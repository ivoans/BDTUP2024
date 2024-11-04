CREATE TABLE Inventario (
    ProductoId INT PRIMARY KEY AUTO_INCREMENT,
    NombreProducto VARCHAR(100) NOT NULL,
    Cantidad INT NOT NULL,
    Precio DECIMAL(10,2) NOT NULL
);

CREATE TABLE HistorialInventario (
    HistorialId INT PRIMARY KEY AUTO_INCREMENT,
    ProductoId INT,
    FechaCambio DATETIME NOT NULL,
    Cambio INT NOT NULL, -- Puede ser positivo o negativo
    Motivo VARCHAR(255) NOT NULL,
	FOREIGN KEY (ProductoId) REFERENCES Inventario(ProductoId)
);