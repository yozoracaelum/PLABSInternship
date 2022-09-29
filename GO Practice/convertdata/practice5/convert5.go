package main

import (
	"fmt"
	"strconv"
)

func main() {
	var num = int64(24)
	var str = strconv.FormatInt(num, 8)

	fmt.Println(str)
}
