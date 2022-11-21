package com.ssafy.temproom

data class ChattingItem(
    var firebaseKey: String,
    val name: String,
    val message: String,
    val time: Long
) {
    constructor() : this("", "", "", 1L)
}