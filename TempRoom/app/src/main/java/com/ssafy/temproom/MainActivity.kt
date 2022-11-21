package com.ssafy.temproom

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.ssafy.temproom.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.apply {
            btn.setOnClickListener {
                val intent = Intent(this@MainActivity, SecondActivity::class.java)
                val id = id.text.toString()
                intent.putExtra("id", id)
                startActivity(intent)
            }
        }
    }
}