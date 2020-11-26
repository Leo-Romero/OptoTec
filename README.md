# Trabajo Final Curso 2020 Polotic Misiones

### Características

Sistema web en Django y Javascript para una clínica de Optometría.

##### Requerimientos:
+ Un sistema con un login de usuario con los siguientes roles:
    + Secretaría
    + Profesional medico
    + Ventas
    + Taller
    + Gerencia
+ El sistema gestionará tres Modelos esenciales:
    + Turnos
    + Pedidos
    + Pacientes
+ El rol de Secretaría permite agregar, modificar o eliminar los turnos de los Pacientes.
+ Cada Paciente tiene su historial médico (solo el Profesional médico puede agregar observaciones al historial médico).
+ Cada Profesional médico puede ver el listado de Pacientes filtrando por día, mes o año.
+ El Profesional médico solo puede ver los Pacientes asignados a él.
+ El rol de Ventas puede generar un pedido para el Paciente, donde detalla el Producto que quiere adquirir, el precio (pueden ser más de un producto), un subtotal, tipo de pago (tarjeta de crédito, debido, billetera virtual o efectivo).
    + El producto tiene nombre, si está clasificado como Lente tendrá la opción de Lejos/Cerca, Izquierda/Derecha, si incluye Armazón o no.
    + Una vez que se genera el pedido queda en estado “Pendiente”.
    + Luego el rol de Ventas puede cambiar el estado a “Pedido” o mandarlo a “Taller”.
+ El rol de Taller solo visualiza la lista de pedidos (con todos los detalles del producto sin los precios). El Taller puede confirmar cambiando el estado del pedido a “Finalizado”.
+ Gerencia puede visualizar todos los datos y necesita los siguientes reportes:
    + Pacientes que asistieron a los turnos en la semana/mes.
    + Pacientes que no asistieron a los turnos en la semana/mes.
    + Pacientes que hicieron por lo menos un Pedido en la semana/mes.
    + Productos más vendidos en el mes.
    + Ventas totales por mes clasificadas por Vendedores.

#### V 0.0.1

### Django v2.2.0 final

### Autor
(C) 2020 Leonardo Romero


###End
