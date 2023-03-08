package saphie

import "net/http"

func StartServer() {
	fs := http.FileServer(http.Dir("./static/dist"))
	http.Handle("/dist/", http.StripPrefix("/dist/", fs))
	img := http.FileServer(http.Dir("./assets"))
	http.Handle("/assets/", http.StripPrefix("/assets/", img))
	http.ListenAndServe(":8080", nil)
}
