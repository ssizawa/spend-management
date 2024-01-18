$(function(){
    $('.delete').on('click', function(){
      var nameTag = $(this).attr('name');
      var taskName = nameTag.split('&')[0];
      var taskDescription = nameTag.split('&')[1];
  
      if(confirm('Do you want delete "' + taskName + '"?')){
        $.post('/delete_recode', 'spendName=' + taskName + '&price=' + taskDescription);
      }
      console.log(taskName, taskDescription)
      location.reload();
    });
  });