package main

import "fmt"

var data = map[string]interface{}{
	"nama":    "Julian Evan",
	"grade":   "3rd year",
	"height":  178.56,
	"isMale":  true,
	"hobbies": []string{"Making games", "Drawing"},
}

func main() {
	fmt.Println(data["nama"].(string))
	fmt.Println(data["grade"].(string))
	fmt.Println(data["height"].(float64))
	fmt.Println(data["isMale"].(bool))
	fmt.Println(data["hobbies"].([]string))
}
