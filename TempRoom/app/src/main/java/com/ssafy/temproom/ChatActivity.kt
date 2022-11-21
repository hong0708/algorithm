package com.ssafy.temproom

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.google.firebase.database.DatabaseReference
import com.ssafy.temproom.databinding.ActivityChatBinding

class ChatActivity : AppCompatActivity(){
    private lateinit var myRef: DatabaseReference

    // chatting data list
    private val chatList = mutableListOf<ChattingItem>()
    private lateinit var chatAdapter: ChatItemAdapter

    private lateinit var binding: ActivityChatBinding

    private lateinit var roomId: String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityChatBinding.inflate(layoutInflater)
        setContentView(binding.root)

        roomId = intent.getStringExtra("roomId").toString()

    }


}