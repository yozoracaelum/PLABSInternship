package main

import "fmt"

func mars_age(mars int) int {
	return mars * 365 / 687
}

func main() {
	var age int
	fmt.Scanln(&age)

	mars := mars_age(age)
	fmt.Println(mars)
}
