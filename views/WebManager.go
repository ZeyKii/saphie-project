package saphie

import "net/http"

func StartServer() {
	fs := http.FileServer(http.Dir("../static/dist"))
	http.Handle("/dist/", http.StripPrefix("/dist/", fs))
	img := http.FileServer(http.Dir("../assets"))
	http.Handle("/assets/", http.StripPrefix("/assets/", img))

	http.HandleFunc("/redirect", gotoAuth)
	http.HandleFunc("/authentification", homeHandler)
	http.HandleFunc("/register", Register)
	http.HandleFunc("/login", Login)

	http.HandleFunc("/", Forum)

	http.HandleFunc("/topic", Topic)
	http.HandleFunc("/posting", doPost)
	http.HandleFunc("/post", TmpPost)
	http.HandleFunc("/comment_add", doComment)

	http.HandleFunc("/profile", Profile)
	http.HandleFunc("/upload", UploadFile)
	http.ListenAndServe(":8080", nil)
}
