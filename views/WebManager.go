package saphie

import (
	"html/template"
	"net/http"
)

func StartServer() {
	fs := http.FileServer(http.Dir("./static/dist/"))
	http.Handle("/static/dist/", http.StripPrefix("/static/dist/", fs))
	http.ListenAndServe(":8080", nil)

	http.HandleFunc("/", Main_Page)
}

func Main_Page(w http.ResponseWriter, r *http.Request) {
	tpl := template.Must(template.ParseFiles("/static/dist/index.html"))
	tpl.Execute(w, nil)
}
