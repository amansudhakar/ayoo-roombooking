"""MySQL connection, schema initialization, and demo room data for Ayoo! Rooms."""
import os
import mysql.connector as msq
from tkinter.messagebox import showerror
import sys

DB_HOST = os.getenv("AYOO_DB_HOST", "localhost")
DB_PORT = int(os.getenv("AYOO_DB_PORT", "3306"))
DB_USER = os.getenv("AYOO_DB_USER", "root")
DB_PASSWORD = os.getenv("AYOO_DB_PASSWORD", "")
DB_NAME = "ayoo"

# Preserve the original sample records while making initialization repeatable.
DEMO_ACCOUNT = ("demo_user", "demo1234", "Demo User", 9000000000, None, "ADDD")

sample_data = [
    (123, 'Double', 'Mumbai', 5000, 'TRUE'),
    (124, 'Single', 'Delhi', 3000, 'TRUE'),
    (125, 'Suite', 'Bangalore', 8000, 'TRUE'),
    (126, 'Single', 'Chennai', 3200, 'TRUE'),
    (127, 'Double', 'Kolkata', 4500, 'TRUE'),
    (128, 'Suite', 'Hyderabad', 8500, 'TRUE'),
    (129, 'Double', 'Pune', 4700, 'TRUE'),
    (130, 'Single', 'Ahmedabad', 2900, 'TRUE'),
    (131, 'Suite', 'Jaipur', 8200, 'TRUE'),
    (132, 'Double', 'Lucknow', 4300, 'TRUE'),
    (133, 'Single', 'Kanpur', 3100, 'TRUE'),
    (134, 'Suite', 'Nagpur', 8400, 'TRUE'),
    (135, 'Double', 'Indore', 4800, 'TRUE'),
    (136, 'Single', 'Bhopal', 2950, 'TRUE'),
    (137, 'Suite', 'Patna', 8300, 'TRUE'),
    (138, 'Double', 'Ludhiana', 4600, 'TRUE'),
    (139, 'Single', 'Agra', 3050, 'TRUE'),
    (140, 'Suite', 'Nashik', 8500, 'TRUE'),
    (141, 'Double', 'Vadodara', 4400, 'TRUE'),
    (142, 'Single', 'Surat', 3000, 'TRUE'),
    (143, 'Suite', 'Rajkot', 8300, 'TRUE'),
    (144, 'Double', 'Mumbai', 5100, 'TRUE'),
    (145, 'Single', 'Delhi', 3100, 'TRUE'),
    (146, 'Suite', 'Bangalore', 8100, 'TRUE'),
    (147, 'Single', 'Chennai', 3300, 'TRUE'),
    (148, 'Double', 'Kolkata', 4600, 'TRUE'),
    (149, 'Suite', 'Hyderabad', 8600, 'TRUE'),
    (150, 'Double', 'Pune', 4800, 'TRUE'),
    (151, 'Single', 'Ahmedabad', 3000, 'TRUE'),
    (152, 'Suite', 'Jaipur', 8300, 'TRUE'),
    (153, 'Double', 'Lucknow', 4400, 'TRUE'),
    (154, 'Single', 'Kanpur', 3200, 'TRUE'),
    (155, 'Suite', 'Nagpur', 8500, 'TRUE'),
    (156, 'Double', 'Indore', 4900, 'TRUE'),
    (157, 'Single', 'Bhopal', 3050, 'TRUE'),
    (158, 'Suite', 'Patna', 8400, 'TRUE'),
    (159, 'Double', 'Ludhiana', 4700, 'TRUE'),
    (160, 'Single', 'Agra', 3150, 'TRUE'),
    (161, 'Suite', 'Nashik', 8600, 'TRUE'),
    (162, 'Double', 'Vadodara', 4500, 'TRUE'),
    (163, 'Single', 'Surat', 3100, 'TRUE'),
    (164, 'Suite', 'Rajkot', 8400, 'TRUE'),
    (165, 'Double', 'Mumbai', 5200, 'TRUE'),
    (166, 'Single', 'Delhi', 3200, 'TRUE'),
    (167, 'Suite', 'Bangalore', 8200, 'TRUE'),
    (168, 'Single', 'Chennai', 3400, 'TRUE'),
    (169, 'Double', 'Kolkata', 4700, 'TRUE'),
    (170, 'Suite', 'Hyderabad', 8700, 'TRUE'),
    (171, 'Double', 'Pune', 4900, 'TRUE'),
    (172, 'Single', 'Ahmedabad', 3100, 'TRUE'),
    (173, 'Suite', 'Jaipur', 8400, 'TRUE'),
    (174, 'Double', 'Lucknow', 4500, 'TRUE'),
    (175, 'Single', 'Kanpur', 3300, 'TRUE'),
    (176, 'Suite', 'Nagpur', 8600, 'TRUE'),
    (177, 'Double', 'Indore', 5000, 'TRUE'),
    (178, 'Single', 'Bhopal', 3150, 'TRUE'),
    (179, 'Suite', 'Patna', 8500, 'TRUE'),
    (180, 'Double', 'Ludhiana', 4800, 'TRUE'),
    (181, 'Single', 'Agra', 3250, 'TRUE'),
    (182, 'Suite', 'Nashik', 8700, 'TRUE'),
    (183, 'Double', 'Vadodara', 4600, 'TRUE'),
    (184, 'Single', 'Surat', 3200, 'TRUE'),
    (185, 'Suite', 'Rajkot', 8500, 'TRUE'),
    (186, 'Double', 'Mumbai', 5300, 'TRUE'),
    (187, 'Single', 'Delhi', 3300, 'TRUE'),
    (188, 'Suite', 'Bangalore', 8300, 'TRUE'),
    (189, 'Single', 'Chennai', 3500, 'TRUE'),
    (190, 'Double', 'Kolkata', 4800, 'TRUE'),
    (191, 'Suite', 'Hyderabad', 8800, 'TRUE'),
    (192, 'Double', 'Pune', 5000, 'TRUE'),
    (193, 'Single', 'Ahmedabad', 3200, 'TRUE'),
    (194, 'Suite', 'Jaipur', 8500, 'TRUE'),
    (195, 'Double', 'Lucknow', 4600, 'TRUE'),
    (196, 'Single', 'Kanpur', 3400, 'TRUE'),
    (197, 'Suite', 'Nagpur', 8700, 'TRUE'),
    (198, 'Double', 'Indore', 5100, 'TRUE'),
    (199, 'Single', 'Bhopal', 3250, 'TRUE'),
    (200, 'Suite', 'Patna', 8600, 'TRUE'),
    (201, 'Double', 'Ludhiana', 4900, 'TRUE'),
    (202, 'Single', 'Agra', 3350, 'TRUE'),
    (203, 'Suite', 'Nashik', 8800, 'TRUE'),
    (204, 'Double', 'Vadodara', 4700, 'TRUE'),
    (205, 'Single', 'Surat', 3300, 'TRUE'),
    (206, 'Suite', 'Rajkot', 8600, 'TRUE'),
    (207, 'Double', 'Mumbai', 5400, 'TRUE'),
    (208, 'Single', 'Delhi', 3400, 'TRUE'),
    (209, 'Suite', 'Bangalore', 8400, 'TRUE'),
    (210, 'Single', 'Chennai', 3600, 'TRUE'),
    (211, 'Double', 'Kolkata', 4900, 'TRUE'),
    (212, 'Suite', 'Hyderabad', 8900, 'TRUE'),
    (213, 'Double', 'Pune', 5100, 'TRUE'),
    (214, 'Single', 'Ahmedabad', 3300, 'TRUE'),
    (215, 'Suite', 'Jaipur', 8600, 'TRUE'),
    (216, 'Double', 'Lucknow', 4700, 'TRUE'),
    (217, 'Single', 'Kanpur', 3500, 'TRUE'),
    (218, 'Suite', 'Nagpur', 8800, 'TRUE'),
    (219, 'Double', 'Indore', 5200, 'TRUE'),
    (220, 'Single', 'Bhopal', 3350, 'TRUE'),
    (221, 'Suite', 'Patna', 8700, 'TRUE'),
    (222, 'Double', 'Ludhiana', 5000, 'TRUE'),
    (223, 'Single', 'Agra', 3450, 'TRUE'),
    (224, 'Suite', 'Nashik', 8900, 'TRUE'),
    (225, 'Double', 'Vadodara', 4800, 'TRUE'),
    (226, 'Single', 'Mumbai', 3100, 'TRUE'),
    (227, 'Double', 'Delhi', 4700, 'TRUE'),
    (228, 'Suite', 'Bangalore', 8300, 'TRUE'),
    (229, 'Villa', 'Chennai', 12000, 'TRUE'),
    (230, 'Cottage', 'Kolkata', 6000, 'TRUE'),
    (231, 'Suite', 'Hyderabad', 8500, 'TRUE'),
    (232, 'Double', 'Pune', 4700, 'TRUE'),
    (233, 'Bungalow', 'Ahmedabad', 10500, 'TRUE'),
    (234, 'Suite', 'Jaipur', 8300, 'TRUE'),
    (235, 'Villa', 'Lucknow', 13000, 'TRUE'),
    (236, 'Single', 'Kanpur', 3200, 'TRUE'),
    (237, 'Bungalow', 'Nagpur', 9500, 'TRUE'),
    (238, 'Double', 'Indore', 4900, 'TRUE'),
    (239, 'Single', 'Bhopal', 3050, 'TRUE'),
    (240, 'Cottage', 'Patna', 8500, 'TRUE'),
    (241, 'Suite', 'Ludhiana', 4700, 'TRUE'),
    (242, 'Single', 'Agra', 3150, 'TRUE'),
    (243, 'Villa', 'Nashik', 14000, 'TRUE'),
    (244, 'Double', 'Vadodara', 4800, 'TRUE'),
    (245, 'Single', 'Surat', 3000, 'TRUE'),
    (246, 'Suite', 'Rajkot', 8300, 'TRUE'),
    (247, 'Cottage', 'Mumbai', 5400, 'TRUE'),
    (248, 'Single', 'Delhi', 3200, 'TRUE'),
    (249, 'Villa', 'Bangalore', 9500, 'TRUE'),
    (250, 'Single', 'Chennai', 3300, 'TRUE'),
    (251, 'Double', 'Kolkata', 4600, 'TRUE'),
    (252, 'Suite', 'Hyderabad', 8600, 'TRUE'),
    (253, 'Double', 'Pune', 4800, 'TRUE'),
    (254, 'Bungalow', 'Ahmedabad', 10200, 'TRUE'),
    (255, 'Cottage', 'Jaipur', 8200, 'TRUE'),
    (256, 'Double', 'Lucknow', 4300, 'TRUE'),
    (257, 'Single', 'Kanpur', 3100, 'TRUE'),
    (258, 'Bungalow', 'Nagpur', 9600, 'TRUE'),
    (259, 'Double', 'Indore', 4900, 'TRUE'),
    (260, 'Single', 'Bhopal', 3150, 'TRUE'),
    (261, 'Suite', 'Patna', 8400, 'TRUE'),
    (262, 'Double', 'Ludhiana', 4700, 'TRUE'),
    (263, 'Single', 'Agra', 3200, 'TRUE'),
    (264, 'Cottage', 'Nashik', 8700, 'TRUE'),
    (265, 'Double', 'Vadodara', 4500, 'TRUE'),
    (266, 'Single', 'Surat', 3100, 'TRUE'),
    (267, 'Bungalow', 'Rajkot', 9100, 'TRUE'),
    (268, 'Villa', 'Mumbai', 5300, 'TRUE'),
    (269, 'Single', 'Delhi', 3300, 'TRUE'),
    (270, 'Cottage', 'Bangalore', 8200, 'TRUE'),
    (271, 'Single', 'Chennai', 3400, 'TRUE'),
    (272, 'Double', 'Kolkata', 4700, 'TRUE'),
    (273, 'Bungalow', 'Hyderabad', 8700, 'TRUE'),
    (274, 'Double', 'Pune', 4900, 'TRUE'),
    (275, 'Single', 'Ahmedabad', 3100, 'TRUE'),
    (276, 'Cottage', 'Jaipur', 8400, 'TRUE'),
    (277, 'Double', 'Lucknow', 4400, 'TRUE'),
    (278, 'Single', 'Kanpur', 3200, 'TRUE'),
    (279, 'Bungalow', 'Nagpur', 8600, 'TRUE'),
    (280, 'Double', 'Indore', 5000, 'TRUE'),
    (281, 'Single', 'Bhopal', 3250, 'TRUE'),
    (282, 'Suite', 'Patna', 8500, 'TRUE'),
    (283, 'Double', 'Ludhiana', 4800, 'TRUE'),
    (284, 'Single', 'Agra', 3250, 'TRUE'),
    (285, 'Cottage', 'Nashik', 8800, 'TRUE'),
    (286, 'Double', 'Vadodara', 4600, 'TRUE'),
    (287, 'Single', 'Surat', 3200, 'TRUE'),
    (288, 'Bungalow', 'Rajkot', 8500, 'TRUE'),
    (289, 'Villa', 'Mumbai', 5400, 'TRUE'),
    (290, 'Single', 'Delhi', 3400, 'TRUE'),
    (291, 'Cottage', 'Bangalore', 8300, 'TRUE'),
    (292, 'Single', 'Chennai', 3500, 'TRUE'),
    (293, 'Double', 'Kolkata', 4800, 'TRUE'),
    (294, 'Bungalow', 'Hyderabad', 8800, 'TRUE'),
    (295, 'Double', 'Pune', 5000, 'TRUE'),
    (296, 'Single', 'Ahmedabad', 3200, 'TRUE'),
    (297, 'Cottage', 'Jaipur', 8500, 'TRUE'),
    (298, 'Double', 'Lucknow', 4600, 'TRUE'),
    (299, 'Single', 'Kanpur', 3300, 'TRUE'),
    (300, 'Villa', 'Nagpur', 8700, 'TRUE'),
    (301, 'Double', 'Indore', 5100, 'TRUE'),
    (302, 'Single', 'Bhopal', 3350, 'TRUE'),
    (303, 'Suite', 'Patna', 8600, 'TRUE'),
    (304, 'Double', 'Ludhiana', 4900, 'TRUE'),
    (305, 'Single', 'Agra', 3350, 'TRUE'),
    (306, 'Cottage', 'Nashik', 8900, 'TRUE'),
    (307, 'Double', 'Vadodara', 4700, 'TRUE'),
    (308, 'Single', 'Surat', 3300, 'TRUE'),
    (309, 'Bungalow', 'Rajkot', 8600, 'TRUE'),
    (310, 'Villa', 'Mumbai', 5500, 'TRUE'),
    (311, 'Single', 'Delhi', 3500, 'TRUE'),
    (312, 'Cottage', 'Bangalore', 8400, 'TRUE'),
    (313, 'Single', 'Chennai', 3600, 'TRUE'),
    (314, 'Double', 'Kolkata', 4900, 'TRUE'),
    (315, 'Bungalow', 'Hyderabad', 8900, 'TRUE'),
    (316, 'Double', 'Pune', 5100, 'TRUE'),
    (317, 'Single', 'Ahmedabad', 3300, 'TRUE'),
    (318, 'Cottage', 'Jaipur', 8600, 'TRUE'),
    (319, 'Double', 'Lucknow', 4700, 'TRUE'),
    (320, 'Single', 'Kanpur', 3500, 'TRUE'),
    (321, 'Bungalow', 'Nagpur', 8800, 'TRUE'),
    (322, 'Double', 'Indore', 5200, 'TRUE'),
    (323, 'Single', 'Bhopal', 3400, 'TRUE'),
    (324, 'Cottage', 'Patna', 8700, 'TRUE'),
    (325, 'Double', 'Ludhiana', 5000, 'TRUE'),
    (326, 'Single', 'Agra', 3450, 'TRUE'),
    (327, 'Suite', 'Nashik', 8900, 'TRUE'),
    (328, 'Single', 'New_York', 2000, 'TRUE'),
    (329, 'Double', 'London', 4000, 'TRUE'),
    (330, 'Suite', 'Paris', 7000, 'TRUE'),
    (331, 'Villa', 'Dubai', 12000, 'TRUE'),
    (332, 'Cottage', 'Sydney', 6000, 'TRUE'),
    (333, 'Double', 'Tokyo', 4500, 'TRUE'),
    (334, 'Single', 'Los_Angeles', 2200, 'TRUE'),
    (335, 'Bungalow', 'Singapore', 11000, 'TRUE'),
    (336, 'Suite', 'Rome', 6800, 'TRUE'),
    (337, 'Villa', 'Bangkok', 11500, 'TRUE'),
    (338, 'Single', 'Paris', 3000, 'TRUE'),
    (339, 'Double', 'London', 4200, 'TRUE'),
    (340, 'Bungalow', 'Tokyo', 9500, 'TRUE'),
    (341, 'Villa', 'New_York', 12500, 'TRUE'),
    (342, 'Cottage', 'Sydney', 5800, 'TRUE'),
    (343, 'Double', 'Dubai', 4600, 'TRUE'),
    (344, 'Single', 'Los_Angeles', 2300, 'TRUE'),
    (345, 'Suite', 'Singapore', 7100, 'TRUE'),
    (346, 'Villa', 'Rome', 13000, 'TRUE'),
    (347, 'Cottage', 'Bangkok', 6200, 'TRUE'),
    (348, 'Double', 'Paris', 4800, 'TRUE'),
    (349, 'Single', 'London', 3300, 'TRUE'),
    (350, 'Suite', 'New_York', 7000, 'TRUE'),
    (351, 'Bungalow', 'Tokyo', 9800, 'TRUE'),
    (352, 'Villa', 'Dubai', 13000, 'TRUE'),
    (353, 'Cottage', 'Sydney', 5900, 'TRUE'),
    (354, 'Double', 'Los_Angeles', 4600, 'TRUE'),
    (355, 'Single', 'Singapore', 3200, 'TRUE'),
    (356, 'Suite', 'Rome', 6900, 'TRUE'),
    (357, 'Bungalow', 'Bangkok', 10000, 'TRUE'),
    (358, 'Villa', 'Paris', 12500, 'TRUE'),
    (359, 'Cottage', 'London', 6500, 'TRUE'),
    (360, 'Double', 'New_York', 4700, 'TRUE'),
    (361, 'Single', 'Tokyo', 3400, 'TRUE'),
    (362, 'Bungalow', 'Dubai', 10500, 'TRUE'),
    (363, 'Suite', 'Los_Angeles', 7100, 'TRUE'),
    (364, 'Villa', 'Singapore', 13500, 'TRUE'),
    (365, 'Cottage', 'Rome', 6400, 'TRUE'),
    (366, 'Single', 'Bangkok', 2800, 'TRUE'),
    (367, 'Double', 'Paris', 4900, 'TRUE'),
    (368, 'Bungalow', 'Sydney', 9800, 'TRUE'),
    (369, 'Suite', 'London', 6700, 'TRUE'),
    (370, 'Villa', 'Tokyo', 14000, 'TRUE'),
    (371, 'Single', 'Los_Angeles', 2500, 'TRUE'),
    (372, 'Cottage', 'New_York', 5600, 'TRUE'),
    (373, 'Double', 'Singapore', 4700, 'TRUE'),
    (374, 'Villa', 'Bangkok', 12500, 'TRUE'),
    (375, 'Bungalow', 'Paris', 10500, 'TRUE'),
    (376, 'Single', 'Rome', 3000, 'TRUE'),
    (377, 'Cottage', 'London', 6200, 'TRUE'),
    (378, 'Suite', 'Dubai', 7100, 'TRUE'),
    (379, 'Double', 'Tokyo', 4600, 'TRUE'),
    (380, 'Single', 'Sydney', 3100, 'TRUE'),
    (381, 'Bungalow', 'Los_Angeles', 11500, 'TRUE'),
    (382, 'Villa', 'Singapore', 14000, 'TRUE'),
    (383, 'Suite', 'New_York', 6900, 'TRUE'),
    (384, 'Single', 'Bangkok', 2700, 'TRUE'),
    (385, 'Double', 'Paris', 5100, 'TRUE'),
    (386, 'Bungalow', 'London', 9800, 'TRUE'),
    (387, 'Villa', 'Rome', 13000, 'TRUE'),
    (388, 'Cottage', 'Tokyo', 5900, 'TRUE'),
    (389, 'Suite', 'Los_Angeles', 7200, 'TRUE'),
    (390, 'Double', 'Dubai', 4800, 'TRUE'),
    (391, 'Single', 'Singapore', 3300, 'TRUE'),
    (392, 'Villa', 'Bangkok', 13500, 'TRUE'),
    (393, 'Bungalow', 'Paris', 11000, 'TRUE'),
    (394, 'Suite', 'Sydney', 7000, 'TRUE'),
    (395, 'Single', 'Tokyo', 3200, 'TRUE'),
    (396, 'Cottage', 'New_York', 5500, 'TRUE'),
    (397, 'Double', 'Singapore', 4600, 'TRUE'),
    (398, 'Bungalow', 'Rome', 10000, 'TRUE'),
    (399, 'Suite', 'London', 6600, 'TRUE'),
    (400, 'Villa', 'Bangkok', 14000, 'TRUE')
]

SCHEMA = (
    """CREATE TABLE IF NOT EXISTS admin (
        admin_id BIGINT PRIMARY KEY,
        passkey VARCHAR(10) NOT NULL
    ) ENGINE=InnoDB""",
    """CREATE TABLE IF NOT EXISTS room (
        Room_no INT PRIMARY KEY,
        Roomtype VARCHAR(20),
        City VARCHAR(50),
        Price DECIMAL(10, 2),
        Availability VARCHAR(5)
    ) ENGINE=InnoDB""",
    """CREATE TABLE IF NOT EXISTS user_data (
        Username VARCHAR(30) PRIMARY KEY,
        Password VARCHAR(100) NOT NULL,
        Name VARCHAR(50) DEFAULT 'Ayoo! User',
        Phone BIGINT NOT NULL,
        Aadhar BIGINT UNIQUE,
        Toggles CHAR(4) DEFAULT 'ADDD'
    ) ENGINE=InnoDB""",
    """CREATE TABLE IF NOT EXISTS bookings (
        Booking_ID INT PRIMARY KEY AUTO_INCREMENT,
        Username VARCHAR(30),
        Room_No INT NOT NULL,
        FOREIGN KEY (Room_No) REFERENCES room(Room_no),
        FOREIGN KEY (Username) REFERENCES user_data(Username)
    ) ENGINE=InnoDB""",
)


def _connection_kwargs(include_database=True):
    settings = {
        "host": DB_HOST,
        "port": DB_PORT,
        "user": DB_USER,
        "password": DB_PASSWORD,
    }
    if include_database:
        settings["database"] = DB_NAME
    return settings


def ayoocon(run=False):
    """Open a connection; run=True connects without selecting ayoo."""
    return msq.connect(**_connection_kwargs(include_database=not run))


def initialize_database():
    """Create project tables and insert any missing sample rooms."""
    server = ayoocon(run=True)
    try:
        cursor = server.cursor()
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` "
            "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
        )
        server.commit()
    finally:
        server.close()

    connection = ayoocon()
    try:
        cursor = connection.cursor()
        for statement in SCHEMA:
            cursor.execute(statement)
        cursor.execute(
            "INSERT IGNORE INTO user_data "
            "(Username, Password, Name, Phone, Aadhar, Toggles) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            DEMO_ACCOUNT,
        )
        cursor.executemany(
            "INSERT IGNORE INTO room "
            "(Room_no, Roomtype, City, Price, Availability) "
            "VALUES (%s, %s, %s, %s, %s)",
            sample_data,
        )
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


try:

    if sys.version_info[:3] > (3, 12, 10):

        showerror(title = "Unsupported version", message = "Error: This release is only supported up to Python 3.12.10. You are"
             f" using {sys.version.split()[0]}.")
        raise SystemExit(1)
    
    initialize_database()

except msq.Error as err:

    showerror(
        "MySQL setup failed",
        "Ayoo! Rooms could not connect to MySQL. Confirm MySQL Server is "
        "running, install the project requirements, and set AYOO_DB_PASSWORD "
        f"to your MySQL password.\n\nDetails: {err}",
    )
    raise SystemExit(1)