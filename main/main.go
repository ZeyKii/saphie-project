package main

import (
	"fmt"
	"net/http"
	saphie "saphie/views"
	"text/template"
)

func main() {
	http.HandleFunc("/", Steg_Image)
	http.HandleFunc("/steg-audio", Steg_Audio)
	fmt.Println("Server web lauch on http://localhost:8080")
	saphie.StartServer()
}

func Steg_Image(w http.ResponseWriter, r *http.Request) {
	tmpl := template.Must(template.ParseFiles("./static/steg-image.html"))
	tmpl.Execute(w, nil)
}

func Steg_Audio(w http.ResponseWriter, r *http.Request) {
	tmpl := template.Must(template.ParseFiles("./static/steg-audio.html"))
	tmpl.Execute(w, nil)
}