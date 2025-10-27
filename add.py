import FreeCAD
import Mesh
import os
import datetime
import sys

try:
    doc = FreeCAD.newDocument("test")

    current_dir = "C:/Users/admin/Desktop/hand/models"

    ply_files = [os.path.join(current_dir, f) for f in os.listdir(current_dir) if f.endswith('.ply')]
    ply_files.sort()

    print(f"Найдено PLY файлов: {len(ply_files)}")

    for ply_file in ply_files:
        try:
            mesh = Mesh.Mesh()
            mesh.read(ply_file)
            name = os.path.basename(ply_file)[:-4]
            mesh_object = doc.addObject("Mesh::Feature", name)
            mesh_object.Mesh = mesh
            mesh_object.Placement.Base = FreeCAD.Vector(0, 0, 0)
            print(f"Успешно импортирован: {name}")
        except Exception as e:
            print(f"Ошибка: {e}")

    doc.recompute()
    save_path = "C:/Users/admin/Desktop/hand/test.FCStd"
    if os.path.exists(save_path):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        save_path = f"C:/Users/admin/Desktop/hand/test_{timestamp}.FCStd"
    
    doc.saveAs(save_path)
    print(f"Сохранен: {save_path}")
    
  
    FreeCAD.closeDocument(doc.Name)
    
except Exception as e:
    print(f"Критическая ошибка: {e}")
finally:
    sys.exit(0)