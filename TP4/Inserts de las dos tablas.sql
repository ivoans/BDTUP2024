INSERT INTO Inventario (NombreProducto, Cantidad, Precio) VALUES
('Producto A', 50, 10.50),
('Producto B', 30, 20.00),
('Producto C', 100, 5.75),
('Producto D', 75, 15.30),
('Producto E', 20, 50.00),
('Producto F', 10, 100.00),
('Producto G', 5, 250.00),
('Producto H', 80, 8.25),
('Producto I', 40, 12.50),
('Producto J', 60, 30.00);

INSERT INTO HistorialInventario (ProductoId, FechaCambio, Cambio, Motivo) VALUES
(1, '2024-10-01', -10, 'Venta'),
(2, '2024-10-02', -5, 'Venta'),
(3, '2024-10-03', 20, 'Reabastecimiento'),
(4, '2024-10-04', -15, 'Venta'),
(5, '2024-10-05', 10, 'Reabastecimiento'),
(6, '2024-10-06', -2, 'Venta'),
(7, '2024-10-07', 5, 'Ajuste de inventario'),
(8, '2024-10-08', -8, 'Venta'),
(9, '2024-10-09', -10, 'Devolución'),
(10, '2024-10-10', 15, 'Reabastecimiento');