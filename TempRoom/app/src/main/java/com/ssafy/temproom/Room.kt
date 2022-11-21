package com.ssafy.temproom

data class Room(
    var firebaseKey: String = "",
    // 벙제
    var title: String = "",
    // 호스트
    var host: String = "",
    // 참여 인원
    var count: Int = 1,
    // 참여자들
    var people: ArrayList<String> = ArrayList<String>(),
    // 주제
    var theme: ArrayList<String> = ArrayList<String>(),
    // 남은시간
    var time: Float = 1F,
    // 범인
    var lair: String = "",
) {
    val p = ArrayList<String>()
    val t = ArrayList<String>()
    //constructor() : this("", "", "", 3,p, t, 1111F, id)
}