package com.ssafy.temproom

import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.ssafy.temproom.databinding.ItemListBinding

private const val TAG = "RoomAdapter_싸피"

class RoomAdapter(val list: MutableList<Room>/*, val name: String*/) :
    RecyclerView.Adapter<RoomAdapter.RoomHolder>() {

    inner class RoomHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        fun bindingInfo(item: Room) {
            binding.text.text = item.title

            itemView.setOnClickListener {
                Log.d(TAG, "bindInfo: ${item.title}")
                itemClickListner.onClick(it, layoutPosition, item.title)
            }
        }
    }

    private lateinit var binding: ItemListBinding
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RoomHolder {
        binding = ItemListBinding.inflate(LayoutInflater.from(parent.context))
        return RoomHolder(binding.root)
    }

    override fun onBindViewHolder(holder: RoomHolder, position: Int) {
        holder.bindingInfo(list[position])
    }

    override fun getItemCount(): Int = list.size

    //클릭 인터페이스 정의 사용하는 곳에서 만들어준다.
    interface ItemClickListener {
        fun onClick(view: View, position: Int, roomTitle: String)
    }

    //클릭리스너 선언
    private lateinit var itemClickListner: ItemClickListener

    //클릭리스너 등록 매소드
    fun setItemClickListener(itemClickListener: ItemClickListener) {
        this.itemClickListner = itemClickListener
    }
}