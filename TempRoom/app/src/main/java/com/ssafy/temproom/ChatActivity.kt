package com.ssafy.temproom

import android.os.Build
import android.os.Bundle
import android.text.TextUtils
import android.util.Log
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatActivity
import com.google.firebase.database.ChildEventListener
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.ktx.database
import com.google.firebase.database.ktx.getValue
import com.google.firebase.ktx.Firebase
import com.ssafy.temproom.databinding.ActivityChatBinding

private const val TAG = "ChatActivity_싸피"
class ChatActivity : AppCompatActivity(){
    private lateinit var myRef: DatabaseReference

    // chatting data list
    private val chatList = mutableListOf<ChattingItem>()
    private lateinit var chatAdapter: ChatItemAdapter

    private lateinit var binding: ActivityChatBinding

    private lateinit var roomId: String
    private lateinit var myId: String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityChatBinding.inflate(layoutInflater)
        setContentView(binding.root)

        roomId = intent.getStringExtra("roomId").toString()
        myId = intent.getStringExtra("myId").toString()
        Log.d(TAG, "onCreate: $roomId $myId")

        chatAdapter = ChatItemAdapter(chatList, myId)
        binding.chatRecycler.apply {
            adapter = chatAdapter
        }

        binding.sendBtn.setOnClickListener {
            val message = binding.messageEt.text.toString()
            if (!TextUtils.isEmpty(message)) {
                Log.d(TAG, "onCreate: $message")
                binding.messageEt.setText("")
                //Firebase 전송.
                myRef.push().setValue(ChattingItem("", myId, message, System.currentTimeMillis()))
            }
        }

        initFirebase()
    }

    private lateinit var childEventListener: ChildEventListener
    private fun initFirebase() {
        val database = Firebase.database
        //Firebase database에서 chat-message를 조회. 없으면 생성.
        myRef = database.getReference("lair-game").child(roomId)

        childEventListener = object : ChildEventListener {
            override fun onChildAdded(snapshot: DataSnapshot, previousChildName: String?) {
                Log.d(TAG, "onChildAdded: $snapshot")
//                val chattingItem = snapshot.getValue(ChattingItem::class.java)
                val chattingItem = snapshot.getValue<ChattingItem>()!!
                Log.d(TAG, "chattingItem: $chattingItem")
                chattingItem.firebaseKey = snapshot.key ?: ""
                Log.d(TAG, "chattingItem: $chattingItem")

                chatList.add(chattingItem)
                //notifyDatasetChanged() 사용을 지양...
                chatAdapter.notifyItemInserted(chatList.size)
                binding.chatRecycler.smoothScrollToPosition(chatList.size)
            }

            override fun onChildChanged(snapshot: DataSnapshot, previousChildName: String?) {

            }

            @RequiresApi(Build.VERSION_CODES.N)
            override fun onChildRemoved(snapshot: DataSnapshot) {
                chatList.removeIf {
                    it.firebaseKey == snapshot.key
                }
                chatAdapter.notifyDataSetChanged()
                binding.chatRecycler.smoothScrollToPosition(chatList.size)
            }

            override fun onChildMoved(snapshot: DataSnapshot, previousChildName: String?) {
                TODO("Not yet implemented")
            }

            override fun onCancelled(error: DatabaseError) {
                TODO("Not yet implemented")
            }

        }

        myRef.addChildEventListener(childEventListener)
    }
}