document.addEventListener('DOMContentLoaded', function() {

    function getPostIdFromUrl() {
        const path = window.location.pathname;
        const pathParts = path.split('/'); // Разделяем URL на части

        // Предполагаем, что URL имеет вид /post/123/ и postId находится на втором месте
        const postIdIndex = pathParts.indexOf('post') + 1;
        return pathParts[postIdIndex] || null; // Возвращаем postId или null, если не найдено
    }

    // Получаем postId из URL
    const postId = getPostIdFromUrl();

    // Пример кнопки лайка с ID "like-button"
    document.getElementById('like-button').addEventListener('click', function(event) {
        // Предотвращаем переход по ссылке или отправку формы
        event.preventDefault();

        // Получаем необходимые данные
        const action = 'like';

        // Отправляем асинхронный запрос на сервер
        sendActionToKafka(postId, action);
    });

    function sendActionToKafka(postId, userId, action) {
        fetch('/send_action/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // 'X-CSRFToken': getCookie('csrftoken')  // Получение CSRF токена
            },
            body: JSON.stringify({
                post_id: postId,
                action: action
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                console.log('Data sent to Kafka successfully');
                // Здесь можно обновить UI, например, увеличить счетчик лайков
            } else {
                console.error('Error sending data to Kafka:', data.message);
            }
        })
        .catch(error => console.error('Error:', error));
    }
});
