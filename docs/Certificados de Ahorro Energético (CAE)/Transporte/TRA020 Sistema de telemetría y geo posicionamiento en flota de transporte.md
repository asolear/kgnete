# 
<button class="md-button md-button--primary" id="download-btn">:fontawesome-solid-file-arrow-down: Descargar PDF</button>
<div id="pdf-render" style="border: 1px solid #ccc; width: 100%; height: auto; overflow: auto;"></div>
<script type="module">
    import * as pdfjsLib from '/js/pdfjs/pdf.mjs';
    document.addEventListener('DOMContentLoaded', function () {
        const url = 'TRA020 Sistema de telemetría y geo posicionamiento en flota de transporte.pdf';
        pdfjsLib.GlobalWorkerOptions.workerSrc = '/js/pdfjs/pdf.worker.mjs';
        const container = document.getElementById('pdf-render');
        function renderPage(pdf, pageNumber) {
            return pdf.getPage(pageNumber).then(page => {
                const viewport = page.getViewport({ scale: 1 });
                const containerWidth = container.clientWidth;
                const scale = containerWidth / viewport.width;
                const scaledViewport = page.getViewport({ scale });
                const canvas = document.createElement('canvas');
                canvas.className = 'pdf-page';
                const context = canvas.getContext('2d');
                canvas.style.width = `${scaledViewport.width}px`;;
                canvas.style.height = `${scaledViewport.height}px`;
                const resolutionScale = 2;
                canvas.height = scaledViewport.height * resolutionScale;
                canvas.width = scaledViewport.width * resolutionScale;
                container.appendChild(canvas);
                const renderContext = {
                    canvasContext: context,
                    viewport: page.getViewport({ scale: scale * resolutionScale })
                };
                return page.render(renderContext).promise;
            });
        }
        pdfjsLib.getDocument(url).promise.then(pdf => {
            console.log('PDF cargado');
            const totalPages = pdf.numPages;
            const renderPromises = [];
            for (let pageNumber = 1; pageNumber <= totalPages; pageNumber++) {
                renderPromises.push(renderPage(pdf, pageNumber));
            }
            return Promise.all(renderPromises);
        }).then(() => {
            console.log('Todas las páginas renderizadas');
        }).catch(reason => {
            console.error(reason);
        });
        const downloadBtn = document.getElementById('download-btn');
        downloadBtn.addEventListener('click', function () {
            window.location.href = url;
        });
    });
</script>
