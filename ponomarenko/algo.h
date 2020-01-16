/*
 *
 * This file is part of the Ponomarenko Noise Estimation algorithm.
 *
 * Copyright(c) 2011 Miguel Colom.
 * miguel.colom@cmla.ens-cachan.fr
 *
 * This file may be licensed under the terms of of the
 * GNU General Public License Version 2 (the ``GPL'').
 *
 * Software distributed under the License is distributed
 * on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
 * express or implied. See the GPL for the specific language
 * governing rights and limitations.
 *
 * You should have received a copy of the GPL along with this
 * program. If not, go to http://www.gnu.org/licenses/gpl.html
 * or write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 */

#ifndef _ALGO_H_
#define _ALGO_H_

//! Main algorithm entry point
/*!
  \param argc Number of arguments passed to the program
  \param argv Array of argc arguments passed to the program
*/
int ponomarenko(float *image, int width, int height,
    int w,  // Block side
    int T,  // Block side
    float p,  // Percentile
    int num_bins,  // Number of bins
    int D,  // Filtering distance
    int curve_filter_iterations,  // Filter curve iterations
    int mean_method,  // Mean computation method
    bool remove_equal_pixels_blocks,  // Flag to remove equal pixels
    float *bin_mean, float *bin_std);  // Returns of the function

#endif
