package main

import "fmt"

func main() {
	var n int
	var a int
	fmt.Scanln(&n)
	arr := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scanln(&a)
		arr[i] = a
	}
	fmt.Println(arr)
}
