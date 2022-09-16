package main

import "fmt"

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
	fmt.Println(cities)
}
