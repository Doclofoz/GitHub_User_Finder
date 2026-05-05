using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Windows.Forms;
using Newtonsoft.Json;

namespace UserSearchApp
{
    public partial class Form1 : Form
    {
        // Наш "база данных" (в реальности тут может быть API)
        List<string> allUsers = new List<string> { "Иван Иванов", "Петр Петров", "Анна Сидорова", "Мария Иванова" };
        
        // Список избранного
        List<string> favorites = new List<string>();
        string filePath = "favorites.json";

        public Form1()
        {
            InitializeComponent();
            LoadFavorites(); // Загружаем при старте
        }

        // Кнопка "Поиск"
        private void btnSearch_Click(object sender, EventArgs e)
        {
            string query = txtSearch.Text.Trim();

            // ПРОВЕРКА: Поле не должно быть пустым
            if (string.IsNullOrEmpty(query))
            {
                MessageBox.Show("Поле поиска не должно быть пустым!");
                return;
            }

            // Логика поиска и отображение в списке
            var results = allUsers.Where(u => u.ToLower().Contains(query.ToLower())).ToList();
            lstResults.DataSource = results;
        }

        // Кнопка "В избранное"
        private void btnAddToFav_Click(object sender, EventArgs e)
        {
            if (lstResults.SelectedItem == null) return;

            string selectedUser = lstResults.SelectedItem.ToString();

            if (!favorites.Contains(selectedUser))
            {
                favorites.Add(selectedUser);
                SaveFavorites();
                MessageBox.Show($"{selectedUser} добавлен в избранное!");
            }
        }

        // СОХРАНЕНИЕ В JSON
        private void SaveFavorites()
        {
            string json = JsonConvert.SerializeObject(favorites, Formatting.Indented);
            File.WriteAllText(filePath, json);
        }

        // ЗАГРУЗКА ИЗ JSON
        private void LoadFavorites()
        {
            if (File.Exists(filePath))
            {
                string json = File.ReadAllText(filePath);
                favorites = JsonConvert.DeserializeObject<List<string>>(json) ?? new List<string>();
            }
        }
    }
}
