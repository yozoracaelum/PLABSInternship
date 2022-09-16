package main

import "fmt"

func main() {
	a := make([]int, 5)
	a[1] = 2
	a[2] = 3
	for _, v := range a {
		fmt.Println(v)
	}
}
