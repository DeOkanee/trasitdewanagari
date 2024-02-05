      //keamanan
      document.addEventListener('contextmenu', function (e) {
        e.preventDefault();
        document.getElementById('overlay').style.display = 'block';
        setTimeout(function () {
            document.getElementById('overlay').style.display = 'none';
        }, 3000); // Menampilkan pesan selama 3 detik
    });