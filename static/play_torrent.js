$(() => {
  $('.button.search').on('click', (e) => {
    e.preventDefault()

    let magnet_link = encodeURIComponent($('#magnet-link').val())

    $.get(`/torrent/${magnet_link}`).then((res) => {
      console.log(res)
    })
  })
})
