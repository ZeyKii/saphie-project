package main

import (
	"fmt"
	"net/http"
	saphie "saphie/views"
	"text/template"
)

func main() {
	http.HandleFunc("/", Index)
	fmt.Println("Server web lauch on http://localhost:8080/")
	saphie.StartServer()
}

func Index(w http.ResponseWriter, r *http.Request) {
	tmpl := template.Must(template.ParseFiles("./static/index.html"))
	tmpl.Execute(w, nil)
}