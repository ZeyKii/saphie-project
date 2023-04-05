package saphie

import (
	"html/template"
	"net/http"
)

func StartServer() {
	fs := http.FileServer(http.Dir("./static/dist"))
	http.Handle("/dist/", http.StripPrefix("/dist/", fs))
	img := http.FileServer(http.Dir("./assets"))
	http.Handle("/assets/", http.StripPrefix("/assets/", img))
	http.ListenAndServe(":8080", nil)

	http.HandleFunc("/", Main_Page)
}

func Main_Page(w http.ResponseWriter, r *http.Request) {
	tpl := template.Must(template.ParseFiles("/static/index.html"))
	tpl.Execute(w, nil)
}
