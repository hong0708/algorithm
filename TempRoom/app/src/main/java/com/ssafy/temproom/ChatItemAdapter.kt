package com.ssafy.temproom

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.ssafy.temproom.databinding.ItemChatMessageBinding

class ChatItemAdapter (val list:MutableList<ChattingItem>, val name:String)
    : RecyclerView.Adapter<ChatItemAdapter.MessageHolder>(){

    inner class MessageHolder(itemView: View): RecyclerView.ViewHolder(itemView) {

        fun bindingInfo(item : ChattingItem){
            //화면에 바인딩...
//            itemView.findViewById<TextView>(R.id.textView)
            if(item.name == name){ //내가 쓴 글.
                binding.otherSide.visibility = View.GONE
                binding.mySide.visibility = View.VISIBLE
                binding.myNameTv.text = item.name
                binding.myMessageTv.text = item.message
                binding.myTimeTv.text = item.time.toString()
            }else{ // 다른사람이 쓴 글.
                binding.otherSide.visibility = View.VISIBLE
                binding.mySide.visibility = View.GONE
                binding.otherNameTv.text = item.name
                binding.otherMessageTv.text = item.message
                binding.otherTimeTv.text = item.time.toString()
            }
        }
    }

    private lateinit var binding: ItemChatMessageBinding
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MessageHolder {
        binding = ItemChatMessageBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return MessageHolder(binding.root)
//        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_chat_message, parent, false)
//        return MessageHolder(view)
    }

    override fun onBindViewHolder(holder: MessageHolder, position: Int) {
        holder.bindingInfo(list[position])
    }

    override fun getItemCount(): Int = list.size

}