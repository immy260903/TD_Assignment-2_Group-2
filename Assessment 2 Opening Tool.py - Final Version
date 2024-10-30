import os
import maya.cmds as cmds

class MayaFileOpener:
    def __init__(self, base_path, base_file, wip_path):
        self.base_path = base_path
        self.base_file = base_file
        self.wip_path = wip_path
        self.dept_paths = {
            "Assets": {
                "Prop": {
                    "Car04": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "prop", "car04", "model", "source"),
                            "WIP": os.path.join(wip_path, "assets", "prop", "car04", "model", "source")
                        },
                        "Rig": {
                            "Publish": os.path.join(base_path, "publish", "assets", "prop", "car04", "rig", "source"),
                            "WIP": os.path.join(wip_path, "assets", "prop", "car04", "rig", "source")
                        }
                    }
                },
                "Character": {
                    "SpiderBot01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "character", "spiderBot01", "model", "source"),
                            "WIP": os.path.join(wip_path, "assets", "character", "spiderBot01", "model", "source")
                        },
                        "Rig": {
                            "Publish": os.path.join(base_path, "publish", "assets", "character", "spiderBot01", "rig", "source"),
                            "WIP": os.path.join(wip_path, "assets", "character", "spiderBot01", "rig", "source")
                        }
                    }
                },
                "SetPiece": {
                    "Vase03": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "vase03", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "vase03", "model")
                        }
                    },
                    "Armchair01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "armchair01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "armchair01", "model")
                        }
                    },
                    "BigLamp01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "bigLamp01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "bigLamp01", "model")
                        }
                    },
                    "Blocks01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "blocks01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "blocks01", "model")
                        }
                    },
                    "Book01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "book01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "book01", "model")
                        }
                    },
                    "Book02": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "book02", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "book02", "model")
                        }
                    },
                    "BooksGroup01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "booksGroup01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "booksGroup01", "model")
                        }
                    },
                    "BooksGroup02": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "booksGroup02", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "booksGroup02", "model")
                        }
                    },
                    "BooksGroup03": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "booksGroup03", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "booksGroup03", "model")
                        }
                    },
                    "Bookshelf01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "bookshelf01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "bookshelf01", "model")
                        }
                    },
                    "Candles01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "candles01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "candles01", "model")
                        }
                    },
                    "Candles02": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "candles02", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "candles02", "model")
                        }
                    },
                    "CeilingLights01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "ceilingLights01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "ceilingLights01", "model")
                        }
                    },
                    "CoffeeTable01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "coffeeTable01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "coffeeTable01", "model")
                        }
                    },
                    "Couch01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "couch01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "couch01", "model")
                        }
                    },
                    "Flowers01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "flowers01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "flowers01", "model")
                        }
                    },
                    "Magazine01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "magazine01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "magazine01", "model")
                        }
                    },
                    "PictureFrame01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "pictureFrame01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "pictureFrame01", "model")
                        }
                    },
                    "RoomSkeleton01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "roomSkeleton01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "roomSkeleton01", "model")
                        }
                    },
                    "Sculpture01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "sculpture01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "sculpture01", "model")
                        }
                    },
                    "Sculpture02": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "sculpture02", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "sculpture02", "model")
                        }
                    },
                    "Sculpture03": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "sculpture03", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "sculpture03", "model")
                        }
                    },
                    "Template": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "template", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "template", "model")
                        }
                    },
                    "Vase01": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "vase01", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "vase01", "model")
                        }
                    },
                    "Vase02": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "setPiece", "vase02", "model"),
                            "WIP": os.path.join(wip_path, "assets", "setPiece", "vase02", "model")
                        }
                    }
                },
                "Set": {
                    "LoungeRoom": {
                        "Model": {
                            "Publish": os.path.join(base_path, "publish", "assets", "set", "loungeRoom", "model", "source"),
                            "WIP": os.path.join(wip_path, "assets", "set", "loungeRoom", "model", "source")
                        }
                    }
                }
            },
            "Shots": {
                "Lng01": {
                    "Lng01_010": {
                        "Animation": {
                            "Publish": os.path.join(base_path, "publish", "sequence", "lng01", "lng01_010", "animation", "source"),
                            "WIP": os.path.join(wip_path, "sequence", "lng01", "lng01_010", "animation", "source")
                        },
                        "Layout": {
                            "Publish": os.path.join(base_path, "publish", "sequence", "lng01", "lng01_010", "layout", "source"),
                            "WIP": os.path.join(wip_path, "sequence", "lng01", "lng01_010", "layout", "source")
                        },
                        "Light": {
                            "Publish": os.path.join(base_path, "publish", "sequence", "lng01", "lng01_010", "light", "source"),
                            "WIP": os.path.join(wip_path, "sequence", "lng01", "lng01_010", "light", "source")
                        }
                    }
                }
            }
        }
        
        # Set the project in Maya
        cmds.workspace(self.base_path, openWorkspace=True)
        
        # Open the base file
        self.open_base_file()
        
        # Create the main window
        if cmds.window("fileOpenerWindow", exists=True):
            cmds.deleteUI("fileOpenerWindow")
        self.window = cmds.window("fileOpenerWindow", title="Maya File Opener", widthHeight=(400, 200))
        
        # Create layout
        cmds.columnLayout(adjustableColumn=True)
        
        # Dropdown for department (Assets, Shots)
        self.dept_menu = cmds.optionMenu(label="Department", changeCommand=self.update_tasks)
        cmds.menuItem(label="Assets")
        cmds.menuItem(label="Shots")
        
        # Dropdown for asset/shot type (Prop, Character, SetPiece, Set, etc.)
        self.type_menu = cmds.optionMenu(label="Type", changeCommand=self.update_names)
        
        # Dropdown for asset/shot name (Car04, SpiderBot01, etc.)
        self.name_menu = cmds.optionMenu(label="Name", changeCommand=self.update_steps)
        
        # Dropdown for pipeline step (Model, Rig, Animation, Layout, Light, etc.)
        self.step_menu = cmds.optionMenu(label="Step", changeCommand=self.update_versions)
        
        # Dropdown for version (WIP or Publish)
        self.version_menu = cmds.optionMenu(label="File Type")
        cmds.menuItem(label="WIP")
        cmds.menuItem(label="Publish")
        
        # Button to browse and open file
        cmds.button(label="Open File", command=self.open_file)
        
        # Show the window
        cmds.showWindow(self.window)
        
    def update_tasks(self, dept):
        cmds.optionMenu(self.type_menu, edit=True, deleteAllItems=True)
        for asset_type in self.dept_paths.get(dept, {}).keys():
            cmds.menuItem(parent=self.type_menu, label=asset_type)
        
    def update_names(self, asset_type):
        cmds.optionMenu(self.name_menu, edit=True, deleteAllItems=True)
        selected_dept = cmds.optionMenu(self.dept_menu, query=True, value=True)
        for asset_name in self.dept_paths[selected_dept][asset_type].keys():
            cmds.menuItem(parent=self.name_menu, label=asset_name)
        
    def update_steps(self, asset_name):
        cmds.optionMenu(self.step_menu, edit=True, deleteAllItems=True)
        selected_dept = cmds.optionMenu(self.dept_menu, query=True, value=True)
        selected_type = cmds.optionMenu(self.type_menu, query=True, value=True)
        
        steps = self.dept_paths[selected_dept][selected_type].get(asset_name, {}).keys()
        for step in steps:
            cmds.menuItem(parent=self.step_menu, label=step)
        if not steps:
            cmds.menuItem(parent=self.step_menu, label="")

    def update_versions(self, step):
        pass  # Add further logic here if needed for version updates
    
    def list_versions(self, file_path):
        versions = [file for file in os.listdir(file_path) if file.endswith(".mb")]
        return sorted(versions)
    
    def open_file(self, *args):
        selected_dept = cmds.optionMenu(self.dept_menu, query=True, value=True)
        selected_type = cmds.optionMenu(self.type_menu, query=True, value=True)
        selected_name = cmds.optionMenu(self.name_menu, query=True, value=True)
        selected_step = cmds.optionMenu(self.step_menu, query=True, value=True)
        selected_version = cmds.optionMenu(self.version_menu, query=True, value=True)
        
        try:
            if selected_step:
                file_path = self.dept_paths[selected_dept][selected_type][selected_name][selected_step][selected_version]
            else:
                file_path = self.dept_paths[selected_dept][selected_type][selected_name][selected_version]
        except KeyError:
            cmds.confirmDialog(title="Error", message="Invalid selection. Please check your choices.", button=["OK"])
            return

        versions = self.list_versions(file_path)
        if versions:
            latest_version = versions[-1]
            file_to_open = os.path.join(file_path, latest_version)
            if os.path.exists(file_to_open):
                cmds.file(file_to_open, open=True, force=True)
                cmds.confirmDialog(title="Success", message="File opened successfully!", button=["OK"])
            else:
                cmds.confirmDialog(title="Error", message="File not found!", button=["OK"])
        else:
            cmds.confirmDialog(title="Error", message="No versions found.", button=["OK"])

    def open_base_file(self):
        if os.path.exists(self.base_file):
            cmds.file(self.base_file, open=True, force=True)
            cmds.confirmDialog(title="Success", message="Base file opened successfully!", button=["OK"])
        else:
            cmds.confirmDialog(title="Error", message="Base file not found!", button=["OK"])

# Initialize with paths
base_folder_path = "C:/Users/imraa/Documents/UTS/Maya/Assessment2_Test_Assets_2024/Assessment2_Test_Assets_v002"
wip_folder_path = "C:/Users/imraa/Documents/UTS/Maya/Assessment2_Test_Assets_2024/Assessment2_Test_Assets_v002/wip"
base_file_path = "C:/Users/imraa/Documents/UTS/Maya/Assessment2_Test_Assets_2024/Assesment 2 Base File.mb"
MayaFileOpener(base_folder_path, base_file_path, wip_folder_path)
