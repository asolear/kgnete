# RES030 Nueva implantación, sustitución o ampliación de instalación térmica en un edificio y piscina con tecnología solar térmica

<button class="md-button md-button--primary" id="download-btn">:fontawesome-solid-file-arrow-down: Descargar PDF</button>
<div id="pdf-render" style="border: 1px solid #ccc; width: 100%; height: auto; overflow: auto;"></div>
<script type="module">
    import * as pdfjsLib from '/js/pdfjs/pdf.mjs';
    document.addEventListener('DOMContentLoaded', function () {
        const url = 'RES030 Nueva implantación, sustitución o ampliación de instalación térmica en un edificio y piscina con tecnología solar térmica.pdf';
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
                canvas.height = scaledViewport.height;
                canvas.width = scaledViewport.width;
                container.appendChild(canvas);
                const renderContext = {
                    canvasContext: context,
                    viewport: scaledViewport
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
