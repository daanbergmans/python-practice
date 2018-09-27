image_1000 = ImageTk.PhotoImage(test_images[1])

imageLabel = tk.Label(root, image=base_image)
imageLabel.image = base_image

imageLabel.pack(side=tk.LEFT)
