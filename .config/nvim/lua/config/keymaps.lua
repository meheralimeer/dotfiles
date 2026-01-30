vim.g.mapleader = " "

local keymap = vim.keymap

-- Window Navigation
keymap.set("n", "<C-h>", "<C-w>h")
keymap.set("n", "<C-j>", "<C-w>j")
keymap.set("n", "<C-k>", "<C-w>k")
keymap.set("n", "<C-l>", "<C-w>l")

-- Clear search highlights
keymap.set("n", "<leader>nh", ":nohl<CR>", { desc = "Clear search highlights" })

-- Fast save/quit
keymap.set("n", "<leader>w", ":w<CR>", { desc = "Save" })
keymap.set("n", "<leader>q", ":q<CR>", { desc = "Quit" })
