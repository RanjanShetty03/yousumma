$(document).ready(function() {
    let player; // Define player variable outside the event handler

    $('#transcriptForm').submit(function(event) {
        event.preventDefault(); 
        document.getElementById('spinner').style.display = 'block';
        
        var videoLink = $('#videoLink').val();
        
        $.ajax({
            type: 'POST',
            url: '/summarize',
            data: {video_link: videoLink},
            success: function(response) {
                document.getElementById('spinner').style.display = 'none';
                $('#summaryResult').show();
                
                // Clear previous results
                $('#summaryContent').empty();
                $('#transcriptContent').empty();
                
                // Update with new results
                $('#summaryContent').html(response.summary);
                $('#transcriptContent').html(response.transcript);
                
                // Destroy previous player instance if exists
                if (player) {
                    player.destroy();
                }

                // Initialize YouTube Player
                player = new YT.Player('player', {
                    height: '360',
                    width: '100%',
                    videoId: response.video_id,
                    playerVars: {
                        'autoplay': 1,
                        'controls': 1
                    },
                    events: {
                        'onReady': onPlayerReady
                    }
                });

                $('#player').css('display', 'block');

                
                // Scroll to the summary result section
                $('html, body').animate({
                    scrollTop: $('#summaryResult').offset().top
                }, 1000);
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });

    // Switch between Summary and Transcript tabs
    $('#summaryTab').click(function() {
        $('#summaryTab').addClass('active');
        $('#transcriptTab').removeClass('active');
        $('#summaryContent').addClass('show active');
        $('#transcriptContent').removeClass('show active');
    });

    $('#transcriptTab').click(function() {
        $('#transcriptTab').addClass('active');
        $('#summaryTab').removeClass('active');
        $('#transcriptContent').addClass('show active');
        $('#summaryContent').removeClass('show active');
    });

    function onPlayerReady(event) {
        event.target.playVideo();
    }
});


function copyText() {
    var textToCopy = $('.tab-pane.active').text();
    navigator.clipboard.writeText(textToCopy)
        .then(() => {
            console.log('Text copied successfully');
        })
        .catch(err => {
            console.error('Error copying text: ', err);
        });
}

function downloadText() {
    var textToDownload = $('.tab-pane.active').text();
    var videoLink = $('#videoLink').val();
    var blob = new Blob([textToDownload + '\n\nVideo Link: ' + videoLink], { type: "text/plain;charset=utf-8" });
    saveAs(blob, "summary.txt");
}

document.getElementById('inputLink').addEventListener('click', function(event) {
    event.preventDefault(); 
    document.getElementById('videoLink').focus();
});

$(document).ready(function() {
    $('html, body').animate({ scrollTop: 0 }, 'fast'); 
});

document.getElementById('but-submit').addEventListener('click', function(event){
    event.preventDefault(); 
    document.getElementById('but-submit').style.backgroundColor='#235789';

    setTimeout(function() {
        document.getElementById('but-submit').style.backgroundColor = '#235789';
    }, 3000); 
});

function downloadZip() {
    var zipFileUrl = '/download_extension';
    var filename = 'yousumma_chrm_extension.crx';
    
    fetch(zipFileUrl)
        .then(response => response.blob())
        .then(blob => saveAs(blob, filename))
        .catch(error => console.error('Error downloading file:', error));
}