from daos.ingredient_dao import IngredientDao

class IngredientService:
    def __init__(self, dao: IngredientDao) -> None:
        self.__dao = dao

    def get_all(self):
        results = self.__dao.get_all_ingredients()
        formatted = [{'id':id, 'name':name, 'storage_category':strg_ctgr} for id, name, strg_ctgr in results]

        return formatted
    
    def get_by_id(self, ingr_id: int):
        id, name, strg_ctgr = self.__dao.get_ingredient_by_id(ingr_id)

        return {'id':id, 'name':name, 'storage_category':strg_ctgr}
    
    def create(self, name: str, category: str):
        if len(name) < 1:
            raise ValueError('Raaka-aineen nimi ei saa olla tyhjä')
        
        if category != 'Kylmä' and category != 'Kuiva':
            raise ValueError('Raaka-aineen katgorian tulee olla "Kylmä" tai "Kuiva"')

        id, name, strg_ctgr = self.__dao.create_ingredient(name=name, storage_category=category)

        return {'id':id, 'name':name, 'storage_category':strg_ctgr}
        