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
<<<<<<< HEAD
	tpl := template.Must(template.ParseFiles("/static/dist/steg-image.html"))
=======
	tpl := template.Must(template.ParseFiles("/static/index.html"))
>>>>>>> 177c9304e7de0bdfc7e1e351ef69e8ac956a1c82
	tpl.Execute(w, nil)
}
