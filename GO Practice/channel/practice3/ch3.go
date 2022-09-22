package main

import "fmt"

func count(x int, a []int, ch chan int) {
	var y int = 0
	for i := 0; i < len(a); i++ {
		if a[i] == x {
			y++
		}
	}
	ch <- y
}
func main() {
	data := []int{12, 45, 88, 42, 0, 98, 102, 42, 77, 42, 1, 8, 7, 55, 4, 12, 87, 90, 42, 42, 11, 2, 6, 53, 90, 100, 4, 32, 8}
	var num int
	fmt.Scanln(&num)

	ch1 := make(chan int)
	ch2 := make(chan int)

	go count(num, data[:len(data)/2], ch1)
	go count(num, data[len(data)/2:], ch2)
	fmt.Println(<-ch1 + <-ch2)
}
