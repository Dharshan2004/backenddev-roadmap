package database

import (
	"gin-crud/models"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var DB *gorm.DB

func InitDB() {
	db, err := gorm.Open(sqlite.Open("todos.db"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}

	db.AutoMigrate(&models.Todo{})

	DB = db
}
