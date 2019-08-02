KindEditor.ready(function(k) {
    var csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    window.editor = k.create('#id_content', {
        resizeType: 1,
        allowPreviewEmoticons: false,
        allowImageRemote: false,
        // 上传请求路径
        uploadJson: '/upload_file/',
        width: '700px',
        height: '400px',
        // 处理csrf验证
        extraFileUploadParams: {
            csrfmiddlewaretoken: csrf_token
        },
    });
});