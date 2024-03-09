# 文件流下载
使用window.URL
window.URL.createObjectURL(new Blob([data]))
      let link = document.createElement('a')
      link.style.display = 'none'
      link.href = url
      link.setAttribute('download', 'excel.xlsx')

      document.body.appendChild(link)
      link.click()

文件下载:
download: function (params) {
    console.log("params: ", params)
    return axios.post('/api/v2/media/download', params, {responseType:"arraybuffer"}).then((resp)=> {
      let blob = new Blob([resp.data], {type:"text/csv"})
      let objectUrl = URL.createObjectURL(blob)
      window.location.href=objectUrl

      // let url = window.URL.createObjectURL(new Blob([data]))
      // let link = document.createElement('a')
      // link.style.display = 'none'
      // link.href = url
      // link.setAttribute('download', 'excel.xlsx')
      //
      // document.body.appendChild(link)
      // link.click()
    })
  },

ref:
https://blog.csdn.net/qq_32340877/article/details/79864462
