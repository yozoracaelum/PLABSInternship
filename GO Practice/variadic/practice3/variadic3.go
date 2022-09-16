package main

import "fmt"

func route(ct ...string) {
	for _, i := range ct {
		fmt.Print(i + "->")
	}
}
func main() {
	var n int
	fmt.Scanln(&n)
	var city string
	//var cities []string
	cities := make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Scanln(&city)
		cities[i] = city
	}
	//fmt.Println(cities)
	route(cities...)
}
