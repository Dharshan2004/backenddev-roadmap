package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	router.GET("/todos", getTodos)
	router.POST("/todos", createTodo)
	router.PUT("/todos/:id", updateTodo)
	router.DELETE("/todos/:id", deleteTodo)
	router.Run(":8080")
}

func getTodos(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{"message": "Hello World"})
}

func createTodo(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{"message": "Hello World"})
}

func updateTodo(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{"message": "Hello World"})
}

func deleteTodo(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{"message": "Hello World"})
}
