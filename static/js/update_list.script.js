let list_friends = $(`#list_friends`);
let search_field = document.querySelector('.input-search')
search_field.oninput = function () {
    $.ajax({
        url: '/user_list/',
        type: 'GET',
        data: {'username': search_field.value},
        beforeSend: function() {
            list_friends.empty();
        },
        success: (response) => {
            list_friends.append(response);
        }
    })
};


function invite_friend(id) {
    $.ajax({
        url: '/invite_friend/',
        type: 'GET',
        data: {'inviter_id': id}
    })
}
