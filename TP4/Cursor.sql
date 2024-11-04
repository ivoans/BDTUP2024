use tp_4;

CREATE TEMPORARY TABLE CambiosInventario (
    ProductoId INT,
    Cambio INT,
    Motivo VARCHAR(255)
)//

DELIMITER //

CREATE PROCEDURE RegistrarCambiosInventario()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE ProductoId INT;
    DECLARE Cambio INT;
    DECLARE Motivo VARCHAR(255);
    DECLARE FechaCambio DATETIME DEFAULT NOW();

    DECLARE CambiosCursor CURSOR FOR
        SELECT ProductoId, Cambio, Motivo FROM CambiosInventario;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    START TRANSACTION;

    BEGIN
        OPEN CambiosCursor;

        read_loop: LOOP
            FETCH CambiosCursor INTO ProductoId, Cambio, Motivo;
            IF done THEN
                LEAVE read_loop;
            END IF;

            UPDATE Inventario
            SET Cantidad = Cantidad + Cambio
            WHERE ProductoId = ProductoId;

            INSERT INTO HistorialInventario (ProductoId, FechaCambio, Cambio, Motivo)
            VALUES (ProductoId, FechaCambio, Cambio, Motivo);
        END LOOP;

        CLOSE CambiosCursor;
        COMMIT;
    END;

    ROLLBACK;
END//

DELIMITER ;
