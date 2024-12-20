package com.example.egzamin

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
        val email_edit_text : EditText = findViewById(R.id.email_edit_text)
        val password_edit_text : EditText = findViewById(R.id.password_edit_text)
        val repeat_password_edit_text : EditText = findViewById(R.id.repeat_password_edit_text)
        val submit_btn : Button = findViewById(R.id.submit_btn)
        val info_text_view : TextView = findViewById(R.id.info_text_view)

        submit_btn.setOnClickListener {
            val password = password_edit_text.text.toString()
            val repeatedPassword = repeat_password_edit_text.text.toString()
            val email = email_edit_text.text.toString()

            when {
                password != repeatedPassword -> info_text_view.text = "Hasła się różnią"
                !email.contains('@') -> info_text_view.text = "Niepoprawny adres email"
                else -> info_text_view.text = "Witaj $email"
            }
        }
        /*

        /********************************************************
         * nazwa funkcji: setOnClickListener
         * parametry wejściowe: brak
         * wartość zwracana: brak , obsluguje walidacje pol rejestracji konta
         * autor: 2137
         * ****************************************************/
        */
    }
}