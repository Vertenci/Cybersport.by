$(document).ready(function() {
        let seconds = 0; // Начальное значение секунд

        function updateTimer() {
            seconds++; // Увеличиваем секунды
            const hours = String(Math.floor(seconds / 3600)).padStart(2, '0'); // Часы
            const minutes = String(Math.floor((seconds % 3600) / 60)).padStart(2, '0'); // Минуты
            const remainingSeconds = String(seconds % 60).padStart(2, '0'); // Остальные секунды
            $('#session-timer').text(`${hours}:${minutes}:${remainingSeconds}`); // Обновляем отображение таймера
        }

        setInterval(updateTimer, 1000); // Обновляем таймер каждую секунду

        $('.edit-btn').on('click', function() {
            const field = $(this).data('field');
            const info = $('.' + field + '-info');
            const editSection = $(this).siblings('.edit-section');

            $(this).hide();
            editSection.show();
            editSection.find('input[name="' + field + '"]').val(info.text().trim());
        });

        $('.cancel-btn').on('click', function() {
            const editSection = $(this).parent('.edit-section');
            const editBtn = editSection.siblings('.edit-btn');

            editSection.hide();
            editBtn.show();
        });

        $('.save-btn').on('click', function(event) {
            event.preventDefault();
            const editSection = $(this).parent('.edit-section');
            const field = $(this).siblings('input').attr('name');
            const newValue = editSection.find('input[name="' + field + '"]').val();

            $.ajax({
                url: "{% url 'update_profile' %}",
                type: 'POST',
                data: {
                    [field]: newValue,
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                },
                success: function(response) {
                    $('.' + field + '-info').text(response[field]);
                    alert('Данные успешно обновлены!');
                    editSection.hide();
                    editSection.siblings('.edit-btn').show();
                },
                error: function(xhr) {
                    alert('Произошла ошибка при обновлении данных.');
                }
            });
        });
    });