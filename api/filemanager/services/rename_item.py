from core.utils import filesystem as cpfs
import os


class RenameItemService(object):
    """Rename item.
    
    This class is responsible to rename a file or a directory.
    """
    
    def __init__(self, request):
        self.request = request
    
    def rename_item(self, validated_data: dict) -> bool:
        """Rename item.
        
        Args:
            validated_data (dict): Validated data from serializer (api.filemanager.serializers.RenameFileSerializer)
        
        Returns:
            bool: True on success and False on failure.
        """
        root_path = validated_data.get('path')
        new_name = validated_data.get('new_name')
        old_name = validated_data.get('old_name')
        user = self.request.user
        
        BASE_PATH = cpfs.get_user_path(user)
            
        if not root_path or not root_path.startswith(BASE_PATH):
            root_path = BASE_PATH
            
        old_path = os.path.join(root_path, old_name)
        new_path = os.path.join(root_path, new_name)
        if os.path.exists(old_path) and not os.path.exists(new_path):
            try:
                os.rename(old_path, new_path)
                return True
            except:
                pass    
        
        return False