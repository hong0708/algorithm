package com.ssafy.temproom

import android.content.Intent
import android.os.Build
import android.os.Bundle
import android.util.Log
import android.view.View
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatActivity
import com.google.firebase.database.ChildEventListener
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.ktx.database
import com.google.firebase.database.ktx.getValue
import com.google.firebase.ktx.Firebase
import com.ssafy.temproom.databinding.ActivitySecondBinding

private const val TAG = "SecondActivity_싸피"

class SecondActivity : AppCompatActivity() {

    private lateinit var binding: ActivitySecondBinding
    private lateinit var id: String

    private lateinit var myRef: DatabaseReference

    // chatting data list
    private val roomList = mutableListOf<Room>()
    private lateinit var roomAdapter: RoomAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySecondBinding.inflate(layoutInflater)
        setContentView(binding.root)

        id = intent.getStringExtra("id").toString()

        val people = ArrayList<String>()
        people.add(id)
        people.add("1")
        people.add("2")
        people.add("3")

        val message = ArrayList<ChattingItem>()

        val data = ArrayList<Room>()
        data.add(
            Room(
                "",
                "",
                "",
                4,
                people,
                people,
                123412321F,
                id
            )
        )

        roomAdapter = RoomAdapter(roomList)
        roomAdapter.setItemClickListener(object : RoomAdapter.ItemClickListener {
            override fun onClick(view: View, position: Int, roomTitle: String) {
                val intent = Intent(this@SecondActivity, ChatActivity::class.java)
                intent.putExtra("roomId", roomTitle)
                intent.putExtra("myId", id)
                startActivity(intent)
            }
        })

        binding.roomRecyclerView.apply {
            adapter = roomAdapter
        }

        initFirebase()

        binding.btn.setOnClickListener {
            myRef.push().setValue(
                Room(
                    "",
                    id,
                    id,
                    4,
                    people,
                    people,
                    123412321F,
                    id
                )
            )
            Log.d(TAG, "onCreate: $roomList")
        }


        binding.delete.setOnClickListener {
            myRef.child("room").child("")
        }
    }

    private lateinit var childEventListener: ChildEventListener
    private fun initFirebase() {
        val database = Firebase.database
        //Firebase database에서 chat-message를 조회. 없으면 생성.
        myRef = database.getReference("lair-game").child("room")

        childEventListener = object : ChildEventListener {
            override fun onChildAdded(snapshot: DataSnapshot, previousChildName: String?) {
                Log.d(TAG, "onChildAdded: $snapshot")
//                val chattingItem = snapshot.getValue(ChattingItem::class.java)
                val roomItem = snapshot.getValue<Room>()!!
                Log.d(TAG, "chattingItem: $roomItem")
                roomItem.firebaseKey = snapshot.key ?: ""
                Log.d(TAG, "chattingItem: $roomItem")

                roomList.add(roomItem)
                //notifyDatasetChanged() 사용을 지양...
                roomAdapter.notifyItemInserted(roomList.size)
                binding.roomRecyclerView.smoothScrollToPosition(roomList.size)
            }

            override fun onChildChanged(snapshot: DataSnapshot, previousChildName: String?) {

            }

            @RequiresApi(Build.VERSION_CODES.N)
            override fun onChildRemoved(snapshot: DataSnapshot) {
                roomList.removeIf {
                    it.firebaseKey == snapshot.key
                }
                roomAdapter.notifyDataSetChanged()
                binding.roomRecyclerView.smoothScrollToPosition(roomList.size)
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