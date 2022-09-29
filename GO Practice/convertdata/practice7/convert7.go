package main

import (
	"fmt"
	"strconv"
)

func main() {
	var num = float64(24.12)
	var str = strconv.FormatFloat(num, 'f', 6, 64)

	fmt.Println(str)
}
