-- CREATE DATABASE VentaDeProductos;

CREATE TABLE Usuario (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido_paterno VARCHAR(100),
    apellido_materno VARCHAR(100),
    edad INTEGER,
    correo_electronico VARCHAR(255),
    telefono VARCHAR(20)
);

CREATE TABLE Categoria (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(100),
    clave VARCHAR(50),
    imagen VARCHAR(255),
    fecha_de_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_de_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario_creacion INTEGER REFERENCES Usuario(id),
    id_usuario_modificacion INTEGER REFERENCES Usuario(id),
    id_usuario_eliminacion INTEGER REFERENCES Usuario(id)
);

CREATE TABLE Producto (
    id SERIAL PRIMARY KEY,
    codigo_de_producto VARCHAR(50),
    nombre VARCHAR(150),
    descripcion TEXT,
    id_categoria INTEGER REFERENCES Categoria(id),
    imagen VARCHAR(255),
    precio DECIMAL(14, 4),
    existencias INTEGER,
    codigo_de_barras VARCHAR(50),
    fecha_de_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_de_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario_creacion INTEGER REFERENCES Usuario(id),
    id_usuario_modificacion INTEGER REFERENCES Usuario(id),
    id_usuario_eliminacion INTEGER REFERENCES Usuario(id)
);

CREATE TABLE Venta (
    id SERIAL PRIMARY KEY,
    comentarios TEXT,
    id_cajero INTEGER REFERENCES Usuario(id),
    monto DECIMAL(14, 4),
    cambio DECIMAL(14, 4),
    efectivo_pagado DECIMAL(14, 4),
    subtotal DECIMAL(14, 4),
    impuestos DECIMAL(14, 4),
    fecha_de_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_de_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario_creacion INTEGER REFERENCES Usuario(id),
    id_usuario_modificacion INTEGER REFERENCES Usuario(id),
    id_usuario_eliminacion INTEGER REFERENCES Usuario(id)
);

CREATE TABLE DetalleVenta (
    id SERIAL PRIMARY KEY,
    cantidad INTEGER,
    id_venta INTEGER REFERENCES Venta(id),
    id_producto INTEGER REFERENCES Producto(id),
    observaciones TEXT,
    fecha_de_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_de_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario_creacion INTEGER REFERENCES Usuario(id),
    id_usuario_modificacion INTEGER REFERENCES Usuario(id),
    id_usuario_eliminacion INTEGER REFERENCES Usuario(id)
);

