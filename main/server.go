package main

import (
	"fmt"
	saphie "saphie/views"
)

func main() {
	fmt.Println("Server web lauch on http://localhost:8080/")
	saphie.StartServer()
}
