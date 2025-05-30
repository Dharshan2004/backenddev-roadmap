package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

// hello world handler
func helloHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Printf("%s %s 200 OK\n", r.Method, r.URL.Path)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(map[string]string{"message": "Hello, World!"})
}

func main() {
	http.HandleFunc("/", helloHandler)
	http.ListenAndServe(":8080", nil)
}
