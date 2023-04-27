from django.test import TestCase
from .api import CategoriaViewSet, CursoViewSet

def test():
    #api
    
    

    # Tests that a POST request with invalid data returns a validation error and that a PUT request with invalid data returns a validation error. 
    def test_invalid_data(self, mocker):
        # Arrange
        mock_serializer = mocker.Mock()
        mock_serializer.is_valid.return_value = False
        mocker.patch('app.views.CategoriaSerializer', return_value=mock_serializer)

        view = CategoriaViewSet()
        request = mocker.Mock()
        request.data = {"nome": ""}

        # Act
        response_post = view.post(request)
        response_put = view.put(request, pk=1)

        # Assert
        assert response_post.status_code == 400
        assert response_put.status_code == 400

    # Tests that a GET request returns an empty queryset. 
    def test_empty_queryset(self, mocker):
        # Arrange
        mock_queryset = mocker.Mock()
        mock_queryset.all.return_value = []
        mocker.patch('app.views.Categoria.objects', mock_queryset)

        view = CategoriaViewSet()
        request = mocker.Mock()

        # Act
        response = view.get(request)

        # Assert
        assert response.status_code == 200
        assert len(response.data) == 0

    